let compData = [
    {
    "componeyId" : 1 ,
    "componeyName" : "Harsha Tech Solutions",
    "isHiring" : true,
    "skills" : ["python" , "java" , "html" , "css"],
    "componeydetails":{"address": "Hyd" , "pincode":500081}

    },

    {
    "componeyId" : 2 ,
    "componeyName" : "Techwave Tech Solutions",
    "isHiring" : No,
    "skills" : ["python" , "java" , "html" , "css"],
    "componeydetails":{"address": "Gachebowli" , "pincode":500081}

    }


]
let stringfied = JSON.stringify(compData)  // changing json object to string 
let finalData = JSON.parse(stringfied)      // changing string to json object 
finalData.forEach(students =>{
    console.log('=========================')
    console.log(students)
})