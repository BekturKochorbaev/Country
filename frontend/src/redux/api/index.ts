import {
	BaseQueryFn,
	createApi,
	fetchBaseQuery
} from '@reduxjs/toolkit/query/react';

const getLanguage = (): string => {
	return localStorage.getItem('lang') || 'en';
};


const baseQuery = fetchBaseQuery({
	baseUrl: `${process.env.NEXT_PUBLIC_API_URL}/${getLanguage()}`,
	prepareHeaders: (headers) => {
		let token = JSON.parse(String(localStorage.getItem('accessToken')));
		if (!token) {
			token = JSON.parse(String(sessionStorage.getItem('accessToken')));
		}
		if (token) {
			headers.set('Authorization', `Bearer ${token}`);
		}
		return headers;
	}
});


const baseQueryExtended: BaseQueryFn = async (args, api, extraOptions) => {
	const result = await baseQuery(args, api, extraOptions);
	return result;
};

export const api = createApi({
	reducerPath: 'api',
	baseQuery: baseQueryExtended,
	refetchOnReconnect: true,
	refetchOnFocus: false,
	tagTypes: ['auth', "region", "places", "gallery", "place", "kitchens", 'hotels',"kitchenID", "hotelID", "attractions", "attractionID"],
	endpoints: () => ({})
});
