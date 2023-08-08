import { configureStore } from '@reduxjs/toolkit'
import { rootReducer } from './rootReducers';
import { userAPI } from './../api/core_api';

export default configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware({ serializableCheck: false }).concat([
        userAPI.middleware,
    ]),
})
