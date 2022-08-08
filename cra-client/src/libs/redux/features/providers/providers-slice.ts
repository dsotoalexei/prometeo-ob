/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// TASKS SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { API_ROUTES } from '../../../domains/constants';
import { IProviderModel } from '../../../domains/models';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface IProvidersState {
  providers: IProviderModel[];
  isFetching: boolean;
  isSuccess: boolean;
  isError: boolean;
  errorMessage: string;
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: IProvidersState = {
  providers: [],
  isFetching: false,
  isSuccess: false,
  isError: false,
  errorMessage: '',
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const providersSlice = createSlice({
  name: 'providers',
  initialState,
  reducers: {
    getProviders: (state) => {
      state.isFetching = true;
    },
    getProvidersSuccess: (state, { payload }) => {
      state.providers = payload;
      state.isFetching = false;
      state.isError = false;
    },
    getProvidersFailure: (state) => {
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
export const { getProviders, getProvidersSuccess, getProvidersFailure } =
  providersSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: providersReducer } = providersSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const providersSelector = (state: RootState) => state.providers;
// =============================================================

// =============================================================
// SIDE EFFECTS
// =============================================================
export function fetchProviders() {
  return async (dispatch: any) => {
    dispatch(getProviders());

    try {
      const response = await fetch(`${API_ROUTES.META_PROVIDERS}`);
      const data = await response.json();

      dispatch(getProvidersSuccess(data.providers));
    } catch (error) {
      dispatch(getProvidersFailure());
    }
  };
}
// =============================================================
