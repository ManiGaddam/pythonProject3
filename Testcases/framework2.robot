*** Settings ***
Library    SeleniumLibrary
Library    DataDriver   ../TD/testdata.xlsx

Suite Setup    BrowserOpen
Suite Teardown    BrowserClose
Test Template   LoginPage
*** Variables ***
${browser}  chrome
${url}   https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F


*** Test Cases ***
LoginPage using ${username}



*** Keywords ***
BrowserOpen
    open browser    ${url}    ${browser}
    maximize browser window
    set selenium implicit wait    10 seconds
BrowserClose
    sleep   5
    close browser
LoginPage
    [Arguments]    ${username}  ${password}
    input text    id:Email      ${username}
    input text    id:Password   ${password}
    click element    xpath://button[normalize-space()='Log in']
    page should contain    Login was unsuccessful