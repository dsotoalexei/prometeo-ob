/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// USER SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { API_ROUTES } from '../../../domains/constants';
import { IUserModel } from '../../../domains/models/user.model';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface IUserState {
  user: IUserModel;
  isFetching: boolean;
  isSuccess: boolean;
  isError: boolean;
  errorMessage: string;
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: IUserState = {
  isFetching: false,
  isSuccess: false,
  isError: false,
  errorMessage: '',
  user: {
    name: '',
    document: '',
    email: '',
  },
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    getUser: (state) => {
      state.isFetching = true;
    },
    getUserSuccess: (state, { payload }) => {
      state.user = payload;
      state.isFetching = false;
      state.isError = false;
    },
    getUserFailure: (state) => {
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
export const { getUser, getUserSuccess, getUserFailure } = userSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: userReducer } = userSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const userSelector = (state: RootState) => state.user;
// =============================================================

export function fetchUser() {
  return async (dispatch: any) => {
    dispatch(getUser());

    try {
      const accessKey = localStorage.getItem('accessKey');
      const response = await fetch(`${API_ROUTES.USER_ME}?key=${accessKey}`);
      const data = await response.json();

      dispatch(getUserSuccess(data.info));
    } catch (error) {
      dispatch(getUserFailure());
    }
  };
}
