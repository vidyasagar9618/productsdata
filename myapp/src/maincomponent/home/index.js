import {Component} from 'react'
import Card from '../card'
import Row from '../rowcard'
import TransactionsBarChart from '../TransactionsBarChart';

import "./app.css"




class Mycomponent extends Component {
  state = {
    searchInput:'',
    edata:" ",
    maindata:[],
    bardata:[],
    getvalue:"01"
    
  }

  getdata=async()=>{
    const {getvalue}=this.state
    const response = await fetch(`http://localhost:3005/monthproducts/?month=${getvalue}`)
    const fetchedData = await response.json()
    const converteddata={
        totalSale:fetchedData.totalprice,
        soldItem:fetchedData.sold,
        unsolditems:fetchedData.unsold
    }
    

    this.setState({edata:converteddata})
    
}

getmaindata=async()=>{
  const {getvalue}=this.state
  const response = await fetch(`http://localhost:3005/products/?month=${getvalue}`)
  const fetchedData = await response.json()    
  this.setState({maindata:fetchedData})

}

getbarchatdata=async()=>{
  const {getvalue}=this.state
  const response = await fetch(`http://localhost:3005/ranking/?month=${getvalue}`)
    const barfetchedData = await response.json()
    const h = Object.keys(barfetchedData).map(key => {
      return {
        [key]: barfetchedData[key],
        count:barfetchedData[key],
        range: key
      };
    });
    
    this.setState({bardata:h})
}

componentDidMount(){
this.getdata()
this.getmaindata()
this.getbarchatdata()
}

  

  filterdata=(event)=>{
    this.setState({searchInput: event.target.value})
  }

  sendmonth=(event)=>{
    this.setState({getvalue:event.target.value})
    
  }

  render() {
    const {searchInput,edata,maindata,bardata,getvalue}=this.state
    const filterdata=maindata.filter(each=>each.title.includes(searchInput))
    this.getdata()
    this.getbarchatdata()
    this.getmaindata()

    
    
    return (
      
      <div className='compnentcontainer'>
        <div className='main-container'>
          <div className='iconcontainer'>
                <h3 className='head'>Transaction Dashboard</h3>
          </div>
          <div className='searchContainer'>
            <input type="search" value={searchInput} onChange={this.filterdata} placeholder='Search transaction' className='inputsearch'/>
            <div>
            <label htmlFor="months" className='month'>select month</label>
            <select name="months" id="months" value={getvalue} onChange={this.sendmonth} className='options'>
              <option value="01">jan</option>
              <option value="02">feb</option>
              <option value="03">march</option>
              <option value="04">april</option>
              <option value="05">may</option>
              <option value="06">june</option>
              <option value="07">july</option>
              <option value="08">aug</option>
              <option value="09">sept</option>
              <option value="10">oct</option>
              <option value="11">nov</option>
              <option value="12">dec</option>
            </select>
            </div>
          </div>
          <div>
            <table className="styled-table">
              <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Price</th>
                <th>Description</th>
                <th>Category</th>
                <th>Sold</th>
                <th>Image</th>
              </tr>
                {filterdata.map(each=>(
                  <Row key={each.id} single={each} />
                ))}

            </table>
          </div>

        </div>
        <Card dataty={edata} getvalue={getvalue}/>
      <TransactionsBarChart barfetchedData={bardata} getvalue={getvalue}/> 
        
      </div>
      
      
    )
  }
}

export default Mycomponent
