import './App.css';
import AddressMap from "./Map";
import dispData from "./nys-disp-data";
import 'leaflet/dist/leaflet.css'

function App() {
  return (
    <div className="App">
      <h1> NYS Licensed Dispensary Map</h1>
      <h3> Total Dispensaries: <span>{dispData.numDispensaries}</span></h3>
      <h3> Delivery Only Dispensaries: <span>{dispData.numDeliveryOnly}</span></h3>
      <AddressMap locations={dispData.dispensaries}/>
    </div>
  );
}

export default App;
