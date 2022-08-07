/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// USERS SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface IUsersState {
  loading: boolean;
  hasErrors: boolean;
  users: any[];
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: IUsersState = {
  loading: false,
  hasErrors: false,
  users: [],
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const usersSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    getUsers: (state) => {
      state.loading = true;
    },
    getUsersSuccess: (state, { payload }) => {
      state.users = payload;
      state.loading = false;
      state.hasErrors = false;
    },
    getUsersFailure: (state) => {
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
export const { getUsers, getUsersSuccess, getUsersFailure } =
  usersSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: usersReducer } = usersSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const usersSelector = (state: RootState) => state.users;
// =============================================================

export function fetchUsers() {
  return async (dispatch: any) => {
    dispatch(getUsers());

    try {
      const response = await fetch(
        'https://jsonplaceholder.typicode.com/users'
      );
      const data = await response.json();

      dispatch(getUsersSuccess(data));
    } catch (error) {
      dispatch(getUsersFailure());
    }
  };
}
