import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { baseQuery } from './config'

export const userAPI = createApi({
  reducerPath: 'userAPI', // optional
  baseQuery: baseQuery,
  tagTypes: ['User'],
  endpoints: builder => ({
    getUser: builder.query({
      query: ({ id }) => ({
        url: `/api/users/${id}/`,
        method: 'GET',
      }),
      providesTags: ['User'],
    }),
    addUser: builder.mutation({
      query: (data) => ({
        url: `/api/users/`,
        method: 'POST',
        body: data,
      }),
    })
  })
});

export const { useGetUserQuery, useAddUserMutation } = userAPI;