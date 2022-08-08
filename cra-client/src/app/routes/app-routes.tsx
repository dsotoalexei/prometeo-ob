/**
 * High level router.
 *
 */

import { lazy, Suspense } from 'react';
import { Route, Routes } from 'react-router-dom';
import { isAuthenticatedSelector, useAppSelector } from '../../libs/redux';
import { Loader } from '../../libs/ui/components';
import { ProtectedRoute } from './protected-route';

function AppRoutes() {
  const isAuthenticated = useAppSelector(isAuthenticatedSelector);

  const Layout = lazy(
    () => import('../../libs/ui/components/atoms/layout/layout')
  );
  const Dashboard = lazy(() => import('../pages/dashboard/dashboard.page'));
  const Accounts = lazy(() => import('../pages/accounts/accounts.pages'));
  const CreditCards = lazy(
    () => import('../pages/credit-cards/credit-cards.page')
  );
  const Login = lazy(() => import('../pages/login/login.page'));
  const NotFoundPage = lazy(() => import('../pages/not-found/not-found.page'));

  return (
    <Suspense fallback={<Loader />}>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Layout />}>
          <Route
            index
            element={
              <ProtectedRoute isAuthenticated={isAuthenticated}>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/accounts"
            element={
              <ProtectedRoute isAuthenticated={isAuthenticated}>
                <Accounts />
              </ProtectedRoute>
            }
          />
          <Route
            path="/credit-cards"
            element={
              <ProtectedRoute isAuthenticated={isAuthenticated}>
                <CreditCards />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </Suspense>
  );
}

export { AppRoutes };
