import { configureStore } from '@reduxjs/toolkit';
import { logger } from 'redux-logger';
import {
  persistStore,
  persistReducer,
  FLUSH,
  REHYDRATE,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
} from 'redux-persist';
import storage from 'redux-persist/lib/storage'; // defaults to localStorage for web
import { rootReducer } from './root-reducer';

// ===========================================================================
// PERSIST
// ===========================================================================
// const expireIn = 1 * 60 * 60 * 1000; // expire in 1h
// const expirationKey = 'expirationKey';
const persistConfig = {
  key: 'root',
  storage,
  version: 1,
  whitelist: ['auth'],
  blacklist: [],
};

const persistedReducer = persistReducer(persistConfig, rootReducer);
// ===========================================================================

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
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
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

const persistor = persistStore(store);

export { store, persistor };
