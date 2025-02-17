behave -f allure_behave.formatter:AllureFormatter -o Report\allure_results -D browser=
allure generate Report\allure_results -o Report\allure_report --clean --single-file
allure open Report\allure_report