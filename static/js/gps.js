if(navigator.geolocation){
//判断是否有这个对象
    navigator.geolocation.getCurrentPosition(function(pos){
        show = "经度："+pos.coords.longitude+ " 纬度:"+pos.coords.latitude +"\n"
        if ((pos.coords.longitude < 112.95 && pos.coords.longitude > 112.94)) {
            show += "\n  地理位置验证成功"
        } else {
            show += "\n  地理位置验证失败"
        }
        document.getElementById('location') . innerHTML= show
      // alert("经度："+pos.coords.longitude+
      //   "纬度："+pos.coords.latitude);
      // document.write("经度："+pos.coords.longitude+
      //   "纬度："+pos.coords.latitude)
      //   console.log("经度："+pos.coords.longitude+
      //   "纬度："+pos.coords.latitude);
    })
}else{
    console.log("当前系统不支持GPS API")
}