/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// USER SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface IUserState {
  loading: boolean;
  hasErrors: boolean;
  user: any;
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: IUserState = {
  loading: false,
  hasErrors: false,
  user: {},
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
      state.loading = true;
    },
    getUserSuccess: (state, { payload }) => {
      state.user = payload;
      state.loading = false;
      state.hasErrors = false;
    },
    getUserFailure: (state) => {
      state.loading = false;
      state.hasErrors = true;
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

export function fetchUser(id: string) {
  return async (dispatch: any) => {
    dispatch(getUser());

    try {
      const response = await fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`
      );
      const data = await response.json();

      dispatch(getUserSuccess(data));
    } catch (error) {
      dispatch(getUserFailure());
    }
  };
}
