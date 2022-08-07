import { combineReducers } from 'redux';
import { usersReducer, tasksReducer, userReducer } from '../features';

export const rootReducer = combineReducers({
  users: usersReducer,
  tasks: tasksReducer,
  user: userReducer,
});
