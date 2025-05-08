import React from 'react';
import { Link } from 'react-router-dom';

import HeaderLogo from '@images/headerLogo.png';
import Logout from './Logout';
// import { RequireToken } from '../../Auth';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircle from '@mui/icons-material/AccountCircle';
//import AdbIcon from '@mui/icons-material/Adb';

import {
  AppBar,
  Toolbar,
  CssBaseline,
  Typography,
  Box,
  //useTheme,
  //useMediaQuery,
  styled,
  IconButton,
  Menu,
  MenuItem,
  Button,
  Tooltip,
  //Avatar,
  Container,
} from '@mui/material';
//import Drawer from './Drawer';

// const NavLinks = styled('div')(({ theme }) => ({
//   marginLeft: theme.spacing(5),
//   display: 'flex',
// }));


const NavLink = styled(Link)(() => ({
  
  'textDecoration': 'none',
  'color': 'white',
  // 'fontSize': '20px',
  // 'marginRight': theme.spacing(20),
  '&:hover': {
    color: 'lightblue',
    borderBottom: '1px solid white',
  },
}));

// const LogoBox = () => {
//   return (
//     <Typography
//       component='a'
//       variant='h6'
//       noWrap
//       href='/home'
//       sx={{
//         flexGrow: 1,
//         mr: 2,
//         display: { xs: 'none', md: 'flex' },
//         fontFamily: 'monospace',
//         fontWeight: 700,
//         letterSpacing: '.3rem',
//         color: 'inherit',
//         textDecoration: 'none',
//       }}>
//       <img height="40px"
//         className="img-responsive"
//         src={HeaderLogo}
//         alt="Header Logo"/>
//       </Typography>
//     )
//   };

/**
 *
 * @return {Component} Navbar Component
 */
function Navbar() {
  // const classes = useStyles();
  //const theme = useTheme();
  // const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  //const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  const pages = [
    {
      title: 'Home',
      path: '/home'
    },
    {
      title: 'Import',
      path: '/import'
    },
    {
      title: 'Flight Table',
      path: '/flight-table'
    },
    {
      title: 'Reports',
      path: '/reports'
    }
  ];
  const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  }
  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  }
  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };
  return (
    <>
      <AppBar position="static" 
        style={{ backgroundColor: 'dimgray' }} 
        sx={{ background: 'dimgrey' } }>
        <Container maxWidth="xl">
        <CssBaseline />
        <Toolbar disableGutters>
        <Typography
          component='a'
          variant='h6'
          noWrap
          href='/home'
          sx={{
            mr: 2,
            display: { xs: 'none', md: 'flex' },
            fontFamily: 'monospace',
            fontWeight: 700,
            letterSpacing: '.3rem',
            color: 'inherit',
            textDecoration: 'none',
          }}>
          <img
            height="40px"
            className="img-responsive"
            src={HeaderLogo}
            alt="Header Logo"/>
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none'} }}>
            <IconButton
              size="large"
              color="inherit"
              aria-label="account of current user"
              aria-controls='menu-appbar'
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              >
              <MenuIcon />
            </IconButton>
            <Menu
            id="menu-appbar"
            anchorEl={anchorElNav}
            anchorOrigin={{
              vertical: 'bottom',
              horizontal: 'left',
            }}
            keepMounted
            transformOrigin={{
              vertical: 'top',
              horizontal: 'left',
            }}
            open={Boolean(anchorElNav)}
            onClose={handleCloseNavMenu}
            sx={{
              display: {xs: 'block', md: 'none'}
            }}
            >
              {pages.map((page) => (
                <MenuItem key={page.title} onClick={handleCloseNavMenu}>
                  <NavLink to={`${page.path}`} sx={{textAlign: 'center'}}>
                    {page.title}
                  </NavLink>
                </MenuItem>
              ))}
              </Menu>
          </Box>
          {/* <LogoBox variant="h5" /> */}
          <Typography
            component='a'
            variant='h6'
            noWrap
            href='/home'
            sx={{
              flexGrow: 1,
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}>
            <img
              height="40px"
              className="img-responsive"
              src={HeaderLogo}
              alt="Header Logo"/>
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {pages.map((page) => (
              <Button
                key={page.title}
                onClick={handleCloseNavMenu}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                <NavLink to={`${page.path}`}>
                  {page.title}
                </NavLink>
              </Button>
            ))}
          </Box>
          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <AccountCircle/>
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem sx={{
                  'textDecoration': 'none',
                  'color': 'white',
                  '&:hover': {
                    color: 'lightblue',
                    borderBottom: '1px solid white',
                  },
                  'backgroundColor': 'dimgray',
                }}
                 key={setting} onClick={handleCloseUserMenu}>
                  {setting === 'Logout'? (
                    <Logout component={NavLink} />
                   ) : (
                    <NavLink to={`/${setting.toLowerCase()}`}>
                      {setting}
                    </NavLink>
                   )}
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
        </Container>
      </AppBar>

    </>
  );
}

export default Navbar;
