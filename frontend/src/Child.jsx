import React,{useState} from 'react';

function Child(props){
    const [data,setData] = useState(null);
    const handleClick = () =>{
        const newData = "mashupstack";
        setData(newData);
        props.onDataFromChild(newData);
    }
    const resetClick = () =>{
        props.onDataFromChild(null)
    }
    return(
        <div>
            <button onClick={handleClick} onDoubleClick={resetClick}>click me</button>
            <h2>Data in child componenet:{data}</h2>
        </div>
    )
}
export default Child;