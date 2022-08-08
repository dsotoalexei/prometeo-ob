/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// TASKS SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { API_ROUTES } from '../../../domains/constants';
import { TLoginFormData } from '../../../domains/models/login-form-data.model';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface IAuthState {
  isAuthenticated: boolean;
  isFetching: boolean;
  isSuccess: boolean;
  isError: boolean;
  errorMessage: string;
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: IAuthState = {
  isAuthenticated: false,
  isFetching: false,
  isSuccess: false,
  isError: false,
  errorMessage: '',
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state) => {
      state.isFetching = true;
    },
    loginSuccess: (state, { payload }) => {
      state.isAuthenticated = payload.status === 'logged_in';
      state.isFetching = false;
      state.isError = false;
    },
    loginFailure: (state) => {
      state.isFetching = false;
      state.isError = true;
    },
    logout: (state) => {
      state.isFetching = true;
    },
    logoutSuccess: (state, { payload }) => {
      state.isAuthenticated = payload.status === 'logged_out';
      state.isFetching = false;
      state.isError = false;
    },
    logoutFailure: (state) => {
      state.isFetching = false;
      state.isError = true;
    },
  },
  extraReducers: {},
});
// =============================================================

// =============================================================
// ACTIONS
// =============================================================
export const {
  login,
  loginSuccess,
  loginFailure,
  logout,
  logoutSuccess,
  logoutFailure,
} = authSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: authReducer } = authSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const authSelector = (state: RootState) => state.auth;
export const isAuthenticatedSelector = (state: RootState) =>
  state.auth.isAuthenticated;
// =============================================================

// =============================================================
// SIDE EFFECTS
// =============================================================
export function fetchLogin(formData: TLoginFormData) {
  return async (dispatch: any) => {
    dispatch(login());

    try {
      const response = await fetch(`${API_ROUTES.AUTHENTICATION_LOGIN}`, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      localStorage.setItem('accessKey', data.key);

      dispatch(loginSuccess(data));
    } catch (error) {
      dispatch(loginFailure());
    }
  };
}

export function fetchLogout() {
  return async (dispatch: any) => {
    dispatch(logout());

    try {
      const response = await fetch(`${API_ROUTES.AUTHENTICATION_LOGOUT}`);
      const data = await response.json();

      dispatch(loginSuccess(data));
    } catch (error) {
      dispatch(loginFailure());
    }
  };
}
// =============================================================
