import { combineReducers } from "@reduxjs/toolkit";
import userReducer from './userReducer';
import { userAPI } from './../api/core_api';

export const rootReducer = combineReducers({
    user: userReducer,
    [userAPI.reducerPath]: userAPI.reducer,
})