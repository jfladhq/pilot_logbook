from io import BytesIO
from functools import partial
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape, inch, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer

from fastapi.responses import Response
from sqlalchemy import text

from db.utils import queryset_to_list
def Header(canvas, doc, start, end):
    header_footer = ""
    canvas.saveState()
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="HeaderStyle", Font="Helvetica-Bold", alignment=TA_CENTER, fontSize=20
        )
    )
    styles.add(ParagraphStyle(name="Center", alignment=TA_CENTER, fontName="Helvetica"))
    # Header
    header = Paragraph("Airplane Hours Summary", styles["HeaderStyle"])
    w, h = header.wrap(doc.width, doc.topMargin)
    header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h + 30)

    if start and end:
        header_footer = (
            (datetime.strptime(start, "%Y-%m-%d").strftime("%m/%d/%Y"))
            + " - "
            + (datetime.strptime(end, "%Y-%m-%d").strftime("%m/%d/%Y"))
        )
        # Date Footer
        date_footer = Paragraph(header_footer, styles["Center"])
        w, h = date_footer.wrap(doc.width, doc.bottomMargin)
        date_footer.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h + 2, h)

    canvas.restoreState()

def AirplaneSummaryPDF(db, start=None, end=None, **kwargs):
  summary_top_list = [
    [
      "Airplane",
      "PIC/SIC",
      "Hours",
    ]
  ]
  summary_top_list += queryset_to_list(
    db.execute(text(
      '''
      SELECT 
      a.name,
      p."shortName",
      CAST(SUM(f."totalFlightDuration") as CHAR(8))
      FROM 
      flight f
      INNER JOIN aircraft a on a.id = f.aircraft_id
      INNER JOIN pilottype p on p.id = f.pilotType_id
      GROUP BY a.name, p."shortName";
      '''
    ))
  )
  print(summary_top_list)
  elements = []
  buffer = BytesIO()
  doc = SimpleDocTemplate(
    buffer,
    pagesize=landscape(letter),
    leftMargin=0.1 * inch,
    rightMargin=0.1 * inch,
  )
  doc.title = "Airplane Summary"

  data = summary_top_list
  t = Table(
    data,
    style=[
      ("GRID", (0, 0), (-1, -1), 0.1, colors.black),
      ("FONT", (0, 0), (3, 0), "Helvetica-Bold"),
    ],
  )

  t._argW[0] = 3 * inch
  t._argW[1] = 1 * inch
  t._argW[2] = 1 * inch
  #t._argW[3] = 1 * inch
  #t._argW[4] = 1 * inch
  #t._argW[5] = 1 * inch

  elements.append(Spacer(1, 7.5 * mm))
  elements.append(t)

  doc.build(
    elements,
    onFirstPage=partial(Header, start=start, end=end),
    canvasmaker=NumberedCanvas,
  )

  pdf = buffer.getvalue()
  buffer.close()

  fileName = f"AirplaneSummary-{datetime.now().strftime('%Y-%m-%d')}.pdf"
  response = Response(pdf, media_type="application/pdf")
  response.headers["Content-Disposition"] = "attachment; filename= " + fileName + ""
  
  return response

class NumberedCanvas(canvas.Canvas):
  def __init__(self, *args, **kwargs):
    canvas.Canvas.__init__(self, *args, **kwargs)
    self._saved_page_states = []

  def showPage(self):
    self._saved_page_states.append(dict(self.__dict__))
    self._startPage()

  def save(self):
    """add page info to each page (page x of y)"""
    num_pages = len(self._saved_page_states)
    for state in self._saved_page_states:
      self.__dict__.update(state)
      self.draw_page_number(num_pages)
      canvas.Canvas.showPage(self)

    canvas.Canvas.save(self)

  def draw_page_number(self, page_count):
    # Change the position of this to wherever you want the page number to be
    self.setFont("Helvetica", 10)
    self.drawRightString(770, 15, "Page %d of %d" % (self._pageNumber, page_count))