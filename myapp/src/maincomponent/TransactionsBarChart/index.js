
import "./index.css";

import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Legend,
    ResponsiveContainer,
  } from 'recharts'
  
  

  const TransactionsBarChart =(props)=> {
   
    
      const {barfetchedData,getvalue}=props
     

      const DataFormatter = (number) => {
        return number.toString();
      };
    let g;
    switch (getvalue) {
        case "01":
            g="JAN"
            break;
        case "02":
            g="FEB"
            break;
        case "03":
            g="MARCH"
            break;
        case "04":
            g="APRIL"
            break;
        case "05":
            g="MAY"
            break;
        case "06":
            g="JUNE"
            break;
        case "07":
            g="JULY"
            break;
        case "08":
            g="AUG"
            break;
        case "09":
            g="SEP"
            break;
        case "10":
            g="OCT"
            break;
        case "11":
            g="NOV"
            break;
        case "12":
            g="DEC"
            break;
        default:
            g=0
            break;
    }
    
      return (
        <div className='niii'>
            <h1>Bar Charts stats-{g}<span className="sp">(select month name from dropdown)</span></h1>
      <ResponsiveContainer width="100%" height={500}>
        <BarChart
          data={barfetchedData}
          margin={{
            top: 5,
          }}
        >
          <XAxis
            dataKey="range"
            tick={{
              stroke: "gray",
              strokeWidth: 1,
            }}
          />
          <YAxis
            tickFormatter={DataFormatter}
            tick={{
              stroke: "gray",
              strokeWidth: 0,
            }}
          />
          <Legend
            wrapperStyle={{
              padding: 30,
            }}
          />
          <Bar dataKey="count" name="Items count" fill="#1f77b4" barSize="10%" />
          
        </BarChart>
      </ResponsiveContainer>
      </div>
    )
    



  }


 
  
  




  
export default TransactionsBarChart;
