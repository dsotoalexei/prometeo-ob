/**
 * High level router.
 *
 */

import { lazy, Suspense } from 'react';
import { Route, Routes } from 'react-router-dom';
import { Loader } from '../../libs/ui/components';

function AppRoutes() {
  const Layout = lazy(() => import('../../libs/ui/components/atoms/layout/layout'));
  const Home = lazy(() => import('../pages/home/home.page'));
  const Login = lazy(() => import('../pages/login/login.page'));
  const NotFoundPage = lazy(() => import('../pages/not-found/not-found.page'));

  return (
    <Suspense fallback={<Loader />}>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </Suspense>
  );
}

export { AppRoutes };
