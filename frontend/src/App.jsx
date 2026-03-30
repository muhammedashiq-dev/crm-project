import React,{ useState } from "react"
import Child from './Child'

function App(){
  const [dataFromChild,setDataFromChild] = useState(null);
  const [count,setCount] = useState(0);
  
  function increment(data){
    setDataFromChild(data)
  }
  const countClick = () =>{
    setCount(count + 1)
  }
  return(
    <div>
      <Child onDataFromChild = {increment}/>
      <h2>data from child: {dataFromChild}</h2>
      <button onClick={countClick}>count me</button>
      <h2>Count:{count}</h2>
    </div>
  )
};
export default App;