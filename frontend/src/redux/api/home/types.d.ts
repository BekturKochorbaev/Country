/* eslint-disable @typescript-eslint/no-unused-vars */
namespace HOME {
    type AttractionsResponse = {
        id: number
        attraction_name: string
        region_category: string
        main_image: any
        description: string
        avg_rating: number
        rating_count: number
        popular_places: number
    }[]

    type AttractionsRequest = void
}