import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";


function App() {
  const [partidas, setPartidas] = useState([]);
  const [time, setTime] = useState()

  useEffect(() => {
    axios
      .get("http://localhost:3000/pegar_data")
      .then(async (r) => {
        setPartidas(r.data);
      });
  }, []);

  const pegar_time = () => {
    console.log(time)
    axios
      .get(`http://localhost:3000/pegar_time?nome=${time}`)
      .then(async (r) => {
        setPartidas(r.data);
        console.log(r)
        console.log(partidas)
      });
  }


  return (
    <>
      <input type="text" value={time} onChange={ev => setTime(ev.target.value)}/>
      <button onClick={() => pegar_time()}>data</button>
      {partidas.map((i, id) => (
        <div key={id}>{i.partida}</div>
      ))}
    </>
  );
}

export default App;
