
import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from "leaflet";
import type { LatLngExpression } from 'leaflet';

const unionSquare: LatLngExpression = [40.7359, -73.9911];

type Location = {
  lat: number;
  lng: number;
  name: string;
  address?: string;
  deliveryOnly: boolean;
}

type LocationMarkerProps = {
  location: Location;
}

// idk what the better way to do this is....
const ratio = 1322 / 1154;
const iconHeight = 95;

const nyMarker = L.icon({
    iconUrl: './nymarker.png',
    iconSize: [iconHeight , iconHeight / ratio],
    iconAnchor: [20, 20],
    popupAnchor:  [-10, -10]
})

// find more https://leaflet-extras.github.io/leaflet-providers/preview/#filter=Stadia.AlidadeSmooth
const Stadio_AlidadeSmooth = <TileLayer
    url= "https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png"
    attribution= '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
/>;

const defaultLayer = <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
/>

const LocationMarker: React.FC<LocationMarkerProps> = ({ location }) => {
  return (
    <Marker icon={nyMarker} position={[location.lat, location.lng]}>
      <Popup>
        <strong>{location.name}</strong><br />
        {location.address}<br />
        {location.deliveryOnly ? "Delivery Only" : "In-Person Available"}
      </Popup>
    </Marker>
  );
};

type LocationMapProps = {
  locations: Location[];
}

const LocationMap: React.FC<LocationMapProps> = ({ locations }) => {
  return (
    <MapContainer center={unionSquare} zoom={13} style={{ height: "81vh", width: "100%" }}>
        {Stadio_AlidadeSmooth}
      {locations.map((location, index) => (
        <LocationMarker key={index} location={location} />
      ))}
    </MapContainer>
  );
};

export default LocationMap;
