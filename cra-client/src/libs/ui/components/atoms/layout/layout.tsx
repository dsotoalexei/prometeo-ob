import { Outlet } from 'react-router-dom';
import { NavBar } from '../navbar';
// import { Sidebar } from '../sidebar';
import { LayoutStyled } from './layout.styled';

const Layout = () => {
  return (
    <LayoutStyled>
      <header>
        <NavBar />
      </header>
      <main>
        <Outlet />
      </main>
    </LayoutStyled>
  );
};

export default Layout;
