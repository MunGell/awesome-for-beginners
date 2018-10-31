# Versatile logging with short implementation.
## JavaScript

```javascript
// Superpowered logging for AngularJS.
 
angular.module('logFactory', ['ng'])
 
.value('logFactory_whiteList', /.*/)                                                                                               
//.value('logFactory_whiteList', /!|.*Ctrl|run/)                                                                                   
.value('logFactory_piercingMethods', {warn:true, error:true})                                                                      
                                                                                                                                   
.factory('logFactory', ['$log', 'logFactory_whiteList' , 'logFactory_piercingMethods', function ($log, whiteList, piercing) 
{      
  piercing = piercing || {}                                                                                                        
  whiteList = whiteList || /.*/                                                                                                    
                                                                                                                                   
  return function (prefix, parentLog) {                                                                                            
    var log = parentLog || $log                                                                                                    
    var match = prefix.match(whiteList)                                                                                            
                                                                                                                                   
    function e(fnName) {                                                                                                           
      if (!log[fnName]) {                                                                                                          
        fnName = 'log'                                                                                                             
      }       
                                                                                      
      return (piercing[fnName] || match)                                                                                           
        ? log[fnName].bind(log, '[' + prefix + ']')                                                                                
        : angular.noop                                                                                                             
    }                                                                                                                              
                                                                                                                                   
    return (                                                                                                                       
      { debug: e('debug')                                                                                                          
      , info:  e('info')                                                                                                           
      , log:   e('log')                                                                                                            
      , warn:  e('warn')                                                                                                           
      , error: e('error')                                                                                                          
      }                                                                                                                            
    )                                                                                                                              
  }                                                                                                                                
}
]
)
```
