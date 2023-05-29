export interface Address {
    name: string
    deliveryOnly: boolean
    lat: number
    lng: number
    city: string
    state: string
    address?: string
    zip?: number
    
}

export interface DispData {
    numDeliveryOnly: number,
    numDispensaries: number,
    dispensaries: Array<Address>
}