import { Outlet } from 'react-router-dom';
// import { Sidebar } from '../sidebar';
import { LayoutStyled } from './layout.styled';

const Layout = () => {
  return (
    <LayoutStyled>
      {/* <Sidebar /> */}
      <main>
        <Outlet />
      </main>
    </LayoutStyled>
  );
};

export default Layout;
