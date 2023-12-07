
import './index.css'

const Card=(props)=> {
    const {dataty,getvalue}=props
    const {totalSale,soldItem,unsolditems}=dataty
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

    return(
        <div className="bg-container">
            <h1>Satatistics-{g}</h1>
            <div className="smallcard">
                <div>
                <p>Total sale</p>
                <p>Total sold item </p>
                <p>Total Not sold item</p>
                </div>
                <div className="sales">
                <p>{Math.floor(totalSale)}</p>
                <p>{soldItem}</p>
                <p>{unsolditems}</p>
                </div>

            </div>
        </div>
        )
    }


export default Card;