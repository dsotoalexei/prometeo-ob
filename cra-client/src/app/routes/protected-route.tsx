import { FC } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { ProtectedRouteProps } from './protected-route.types';

const ProtectedRoute: FC<ProtectedRouteProps> = ({
  isAuthenticated,
  children,
  redirectPath = '/login',
}) => {
  if (!isAuthenticated) {
    return <Navigate to={redirectPath} replace />;
  }

  return children ? children : <Outlet />;
};

export { ProtectedRoute };
