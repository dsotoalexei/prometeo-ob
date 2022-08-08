import { ReactElement } from 'react';

export interface ProtectedRouteProps {
  isAuthenticated: boolean;
  children: ReactElement;
  redirectPath?: string;
}
