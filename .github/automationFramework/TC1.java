package automationFramework;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
// Import package pageObject.*
import pageobjects.homepage;
import pageobjects.loginpage;
public class TC1 {

    private static WebDriver driver = null;

   public static void main(String[] args) {

     //driver = new FirefoxDriver();
     driver = new ChromeDriver();
     driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
     driver.get("https://www.store.demoqa.com");
     // Use page Object library now
     homepage.lnk_MyAccount(driver).click();
     loginpage.txtbx_UserName(driver).sendKeys("testuser_1");
     loginpage.txtbx_Password(driver).sendKeys("Test@123");
     loginpage.btn_LogIn(driver).click();

     System.out.println(" Login Successfully, now it is the time to Log Off buddy.");

     homepage.lnk_LogOut(driver).click(); 
     driver.quit();

     }
    
}
