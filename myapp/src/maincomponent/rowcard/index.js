import "./index.css"

const Row=(props)=>{
    const {single}=props
    const {id,title,price,description,category,image,sold}=single
    let f;

    if (sold===1){
        f="True"
    }
    else{
        f="False"
    }
    
    return(
        <tr>
            <td >{id}</td>
            <td >{title}</td>
            <td >{Math.floor(price)}</td>
            <td >{description}</td>
            <td >{category}</td>
            <td >{String(f)}</td>
            <td ><img src={image} alt="imag" className="soldimage"/></td>
        </tr>
    )
    

}

export default Row


