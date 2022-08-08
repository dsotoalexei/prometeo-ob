import { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { ErrorMessage } from '@hookform/error-message';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

import { IProviderModel } from '../../../libs/domains/models';
import {
  fetchProviders,
  fetchLogin,
  providersSelector,
  useAppDispatch,
  useAppSelector,
  authSelector,
  fetchUser,
} from '../../../libs/redux';
import { TLoginFormData } from '../../../libs/domains/models/login-form-data.model';

const loginSchema = yup.object().shape({
  username: yup.string().min(2).max(32).required(),
  password: yup.string().min(5).max(32).required(),
  provider: yup.string().required(),
});

function LoginPage() {
  const dispatch = useAppDispatch();
  let navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    reValidateMode: 'onChange',
    defaultValues: {
      username: '12345',
      password: 'gfdsa',
      provider: 'test',
    },
    mode: 'onChange',
    resolver: yupResolver(loginSchema),
  });
  const { providers, isFetching, isError } = useAppSelector(providersSelector);
  const { isAuthenticated } = useAppSelector(authSelector);

  useEffect(() => {
    dispatch(fetchProviders());
  }, [dispatch]);

  useEffect(() => {
    if (isAuthenticated) {
      dispatch(fetchUser());
      navigate('/', { replace: true });
    }
  }, [dispatch, isAuthenticated, navigate]);

  const onSubmit = (data: TLoginFormData): void => {
    dispatch(fetchLogin(data));
    reset();
  };

  return (
    <div className="container py-16">
      <div className="flex items-center justify-center py-4">
        <img src="assets/images/logo/logo.png" alt="Prometeo" />
      </div>
      <div className="max-w-lg mx-auto shadow px-6 py-7 rounded overflow-hidden">
        <h1 className="text-2xl uppercase font-medium">Iniciar Sesión</h1>
        <p className="text-gray-500 mb-6 text-sm">
          Inicie sesión si es cliente de Prometeo
        </p>
        <form action="" onSubmit={handleSubmit(onSubmit)}>
          <div className="space-y-4">
            <div>
              <label htmlFor="username" className="text-gray-600 mb-2 block">
                Usuario
              </label>
              <input
                {...register('username')}
                type="username"
                className="block w-full border border-gray-300 px-4 py-3 text-gray-600 text-sm rounded focus:ring-0 focus:border-primary placeholder-gray-400"
                placeholder="Enter your email address"
              />
              <span className="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1">
                <ErrorMessage errors={errors} name="username" />
              </span>
            </div>
            <div>
              <label htmlFor="password" className="text-gray-600 mb-2 block">
                Contrase&ntilde;a
              </label>
              <input
                {...register('password')}
                type="password"
                className="block w-full border border-gray-300 px-4 py-3 text-gray-600 text-sm rounded focus:ring-0 focus:border-primary placeholder-gray-400"
                placeholder="Enter your password"
              />
              <span className="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1">
                <ErrorMessage errors={errors} name="password" />
              </span>
            </div>
            <div>
              <label htmlFor="provider" className="text-gray-600 mb-2 block">
                Proveedor
              </label>
              <select
                value="test"
                {...register('provider')}
                disabled={isFetching}
                className="block w-full border border-gray-300 px-4 py-3 text-gray-600 text-sm rounded focus:ring-0 focus:border-primary placeholder-gray-400"
              >
                {isFetching ? (
                  <option value="loading">Cargando proveedores</option>
                ) : isError ? (
                  <option value="error">
                    Problemas al cargar los proveedores
                  </option>
                ) : (
                  providers.map((provider: IProviderModel) => (
                    <option key={provider.code} value={provider.code}>
                      {provider.name}
                    </option>
                  ))
                )}
              </select>
              <span className="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1">
                <ErrorMessage errors={errors} name="provider" />
              </span>
            </div>
          </div>
          <div className="flex items-center justify-center mt-4">
            <button
              type="submit"
              className="inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
            >
              Entrar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export { LoginPage, LoginPage as default };
