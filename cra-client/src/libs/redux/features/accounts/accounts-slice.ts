/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// USERS SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { API_ROUTES } from '../../../domains/constants';
import { IAccountModel } from '../../../domains/models';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface IAccountsState {
  accounts: IAccountModel[];
  isFetching: boolean;
  isSuccess: boolean;
  isError: boolean;
  errorMessage: string;
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: IAccountsState = {
  isFetching: false,
  isSuccess: false,
  isError: false,
  errorMessage: '',
  accounts: [],
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const accountsSlice = createSlice({
  name: 'accounts',
  initialState,
  reducers: {
    getAccounts: (state) => {
      state.isFetching = true;
    },
    getAccountsSuccess: (state, { payload }) => {
      state.accounts = payload;
      state.isFetching = false;
      state.isError = false;
    },
    getAccountsFailure: (state) => {
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
export const { getAccounts, getAccountsSuccess, getAccountsFailure } =
  accountsSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: accountsReducer } = accountsSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const accountsSelector = (state: RootState) => state.accounts;
// =============================================================

export function fetchAccounts() {
  return async (dispatch: any) => {
    dispatch(getAccounts());

    try {
      const accessKey = localStorage.getItem('accessKey');
      const response = await fetch(
        `${API_ROUTES.USER_ACCOUNTS}?key=${accessKey}`
      );
      const data = await response.json();

      dispatch(getAccountsSuccess(data.accounts));
    } catch (error) {
      dispatch(getAccountsFailure());
    }
  };
}
