/* eslint-disable @typescript-eslint/no-explicit-any */
// =============================================================
// TASKS SLICE
// =============================================================
import { createSlice } from '@reduxjs/toolkit';
import { RootState } from '../../setup';

// =============================================================
// MODELS STATE
// =============================================================
interface ITasksState {
  loading: boolean;
  hasErrors: boolean;
  tasks: any[];
}

// =============================================================
// INITIAL STATE
// =============================================================
const initialState: ITasksState = {
  loading: false,
  hasErrors: false,
  tasks: [],
};
// =============================================================

// =============================================================
// SLICE
// =============================================================
export const tasksSlice = createSlice({
  name: 'tasks',
  initialState,
  reducers: {
    getTasks: (state) => {
      state.loading = true;
    },
    getTasksSuccess: (state, { payload }) => {
      state.tasks = payload;
      state.loading = false;
      state.hasErrors = false;
    },
    getTasksFailure: (state) => {
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
export const { getTasks, getTasksSuccess, getTasksFailure } =
  tasksSlice.actions;
// =============================================================

// =============================================================
// REDUCERS
// =============================================================
export const { reducer: tasksReducer } = tasksSlice;
// =============================================================

// =============================================================
// SELECTORS
// =============================================================
export const tasksSelector = (state: RootState) => state.tasks;
// =============================================================


// =============================================================
// SIDE EFFECTS
// =============================================================
export function fetchTasks(userId: string) {
    return async (dispatch: any) => {
      dispatch(getTasks());
  
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/todos?userId=${userId}`
        );
        const data = await response.json();
  
        dispatch(getTasksSuccess(data));
      } catch (error) {
        dispatch(getTasksFailure());
      }
    };
}
// =============================================================

