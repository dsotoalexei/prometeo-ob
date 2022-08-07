import { configureStore } from '@reduxjs/toolkit';
import { logger } from 'redux-logger';

import { rootReducer } from './root-reducer';
// ===========================================================================
// MIDDLEWARES
// ===========================================================================
// eslint-disable-next-line @typescript-eslint/no-explicit-any
let customMiddleware: Array<any> = [];
const isNotProduction = process.env['NODE_ENV'] !== 'production';
if (isNotProduction) {
  customMiddleware = [...customMiddleware, logger];
}
// ===========================================================================

// ===========================================================================
// STORE
// ===========================================================================
const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      thunk: true,
    }).concat(customMiddleware),
  devTools: isNotProduction,
  enhancers: [],
});
// ===========================================================================

// ===========================================================================
// APPLICATION STATE AND DISPATCH
// ===========================================================================
export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
// ===========================================================================

export { store };
