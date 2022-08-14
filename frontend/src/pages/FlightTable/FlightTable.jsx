import React from 'react';
import { Box, Button, IconButton } from '@mui/material';
import ModeEditIcon from '@mui/icons-material/ModeEdit';
import DeleteIcon from '@mui/icons-material/Delete';

import { useFlight } from '@api';
import Table from '@components/Table/Table';

import EditModal from './EditModal';

import './FlightTable.css';


/**
 * Home Page Component
 * @returns {JSX}
 */

const FlightTable = () => {
  const { data, isLoading } = useFlight();
  const [rows, setRows] = React.useState([]);
  const [open, setOpen] = React.useState(false);
  const [editData, setEditData] = React.useState({});
  const handleClose = () => {
    setOpen(false);
    setEditData({});
  };

  const handleOpen = () => {
    setOpen(true);
    setEditData({});
  };

  React.useEffect(() => {
    if (isLoading === false) {
      const newRows = [];
      for (const d of data) {
        newRows.push({ id: d.id, ...d });
      }
      setRows([...newRows]);
    }
  }, [isLoading, data]);

  const columns = React.useMemo(() => [
    {
      field: 'action',
      headerName: 'Action',
      sortable: false,
      width: 120,
      disableColumnMenu: true,
      renderCell: (params) => {
        const onClick = (e) => {
          e.stopPropagation(); // don't select this row after clicking
          // const api = params.api;
          // const thisRow = {};
          // console.log('params', params);
          // api
          //     .getAllColumns()
          //     .filter((c) => c.field !== '__check__' && !!c)
          //     .forEach(
          //         (c) => (thisRow[c.field] = params.getValue(params.id, c.field)),
          //     );
          // console.log('all', api.getAllColumns().filter((c) => c.field !== '__check__' && !!c)
          //     .forEach((c) => console.log('c', c)));
          // console.log('thisRoW', thisRow);
          setOpen(true);
          setEditData(params.row);
        };

        return (
          <>
            <IconButton color="success" onClick={onClick}>
              <ModeEditIcon/>
            </IconButton>
            <IconButton color="error" onClick={onClick}>
              <DeleteIcon/>
            </IconButton>
          </>
        );
      },
    },
    {
      headerName: 'Date',
      field: 'date',
      width: 150,
    },
    {
      headerName: 'Type',
      field: 'aircraftType',
      width: 150,
    },
    {
      headerName: 'Tail',
      field: 'aircraftIdentity',
      width: 150,
    },
    {
      headerName: 'From',
      field: 'fromAirport',
      width: 150,
    },
    {
      headerName: 'To',
      field: 'toAirport',
      width: 150,
    },
    {
      headerName: 'Total Flight Duration',
      field: 'totalFlightDuration',
      width: 150,
    },
    {
      headerName: 'Day Landing',
      field: 'dayLanding',
      width: 150,
    },
    {
      headerName: 'Night Landing',
      field: 'nightLanding',
      width: 150,
    },
    {
      headerName: 'Actual Instrument',
      field: 'actualInstrument',
      width: 150,
    },
    {
      headerName: 'Sim. Instr. Under Hood',
      field: 'simulatedInstrumentUnderHood',
      width: 150,
    },
    {
      headerName: 'ATD Instrument',
      field: 'atdInstrument',
      width: 150,
    },
    {
      headerName: 'Hold',
      field: 'hold',
      width: 150,
    },
    {
      headerName: 'Full Flight Sim.',
      field: 'fullFlightSim',
      width: 150,
    },
    {
      headerName: 'Ground Trainer',
      field: 'groundTrainer',
      width: 150,
    },
    {
      headerName: 'Line Check',
      field: 'lineCheck',
      width: 150,
    },
    {
      headerName: 'Cross Country Time',
      field: 'crossCountryTime',
      width: 150,
    },
    {
      headerName: 'IOE',
      field: 'initialOperatingExperience',
      width: 150,
    },
    {
      headerName: 'Remarks',
      field: 'remarks',
      width: 150,
    },
    {
      headerName: 'Approaches',
      field: 'approaches',
      width: 150,
    },
    {
      headerName: 'Approach Type',
      field: 'approachType',
      width: 150,
    },
    {
      headerName: 'Other Pilot',
      field: 'crewMemberName',
      width: 150,
    },
    {
      headerName: 'Flight Number',
      field: 'flightNumber',
      width: 150,
    },
    {
      headerName: 'Aircraft Category',
      field: 'aircraft_category',
      width: 150,
      renderCell: (params) => {
        return <div className="rowitem">{params.row.aircraft_category.shortName}</div>;
      },
    },
    {
      headerName: 'Pilot Type',
      field: 'pilot_type',
      width: 150,
      renderCell: (params) => {
        return <div className='rowitem'>{params.row.pilot_type.shortName}</div>;
      },
    },
    {
      headerName: 'Airline',
      field: 'airline_identifier',
      width: 150,
      renderCell: (params) => {
        return <div className='rowitem'>{params.row.airline_identifier.name}</div>;
      },
    },
  ], []);


  return (
    <>
      <Box className='flight-table'>
        <Box
          className='flight-table-bg'>
          <center><h1>Flight Table</h1></center>
          <Button variant="contained" color="primary" onClick={handleOpen}>Add</Button>
          {isLoading === false ? <Table rows={rows} columns={columns} /> : null}
        </Box>
      </Box>

      <EditModal open={open} editData={editData} handleClose={handleClose} handleOpen={handleOpen} />
    </>
  );
};

export default FlightTable;
