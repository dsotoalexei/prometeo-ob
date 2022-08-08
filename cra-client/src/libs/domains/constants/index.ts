const API_HOST = process.env.REACT_APP_API_HOST;

export const API_ROUTES = {
  AUTHENTICATION_LOGIN: `${API_HOST}/api/v1/authentication/login/`,
  AUTHENTICATION_LOGOUT: `${API_HOST}/api/v1/authentication/logout/`,
  META_PROVIDERS: `${API_HOST}/api/v1/metas/provider/`,
  USER_ME: `${API_HOST}/api/v1/user/me/`,
  USER_ACCOUNTS: `${API_HOST}/api/v1/user/accounts/`,
  USER_CARDS: `${API_HOST}/api/v1/user/credit-cards/`,
};
