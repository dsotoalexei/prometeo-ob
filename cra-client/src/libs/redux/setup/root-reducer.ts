import { combineReducers } from 'redux';
import {
  accountsReducer,
  cardsReducer,
  providersReducer,
  authReducer,
  userReducer,
} from '../features';

export const rootReducer = combineReducers({
  accounts: accountsReducer,
  cards: cardsReducer,
  providers: providersReducer,
  user: userReducer,
  auth: authReducer,
});
