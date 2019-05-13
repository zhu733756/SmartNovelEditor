const itemKeys = "bookItems";
export default {
  saveItems(val){
    window.localStorage.setItem(itemKeys,JSON.stringify(val))
  },
  readItems(){
    return JSON.parse(window.localStorage.getItem(itemKeys))
  }
}
