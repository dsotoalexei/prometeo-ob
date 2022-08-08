/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// USERS SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { API_ROUTES } from '../../../domains/constants';
import { ICardModel } from '../../../domains/models';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface ICardsState {
  cards: ICardModel[];
  isFetching: boolean;
  isSuccess: boolean;
  isError: boolean;
  errorMessage: string;
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: ICardsState = {
  cards: [],
  isFetching: false,
  isSuccess: false,
  isError: false,
  errorMessage: '',
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const cardsSlice = createSlice({
  name: 'cards',
  initialState,
  reducers: {
    getCards: (state) => {
      state.isFetching = true;
    },
    getCardsSuccess: (state, { payload }) => {
      state.cards = payload;
      state.isFetching = false;
      state.isError = false;
    },
    getCardsFailure: (state) => {
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
export const { getCards, getCardsSuccess, getCardsFailure } =
  cardsSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: cardsReducer } = cardsSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const cardsSelector = (state: RootState) => state.cards;
// =============================================================

export function fetchCards() {
  return async (dispatch: any) => {
    dispatch(getCards());

    try {
      const accessKey = localStorage.getItem('accessKey');
      const response = await fetch(`${API_ROUTES.USER_CARDS}?key=${accessKey}`);
      const data = await response.json();

      dispatch(getCardsSuccess(data.credit_cards));
    } catch (error) {
      dispatch(getCardsFailure());
    }
  };
}
