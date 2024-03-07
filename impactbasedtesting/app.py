import os
import streamlit as st
import generate_coverage_report
import suggest_test_cases
import database
from pathlib import Path

def main():
    
    # Set paths set in config.py
    repo_path               = database.REPO_PATH
    executable_path         = database.EXECUTABLE_PATH
    test_scripts_path       = database.TEST_SCRIPTS_PATH
    result_path             = database.RESULT_PATH
    start_commit            = database.START_COMMIT
    
    reports_path = ""
    try:
        reports_path = Path(os.path.join(database.RESULT_PATH, "coverage_reports"))
        reports_path.mkdir(parents=True, exist_ok=True)
        reports_path.chmod(0o700)
    except Exception as e:
        print(e)
    
    #Scenario from algoaf test case script
    scenario_list = generate_coverage_report.extract_tags(test_scripts_path)
    
    st.header("Impact Based Testing - Demo",)
    col1, col2 = st.columns([1,1])
    
    if col1.button("Execute test cases"):
        with st.spinner('Please Wait!'):
            for scenario in scenario_list:
                # scenario lists xml file
                #xml_file_path = os.path.join(reports_path,f"xml\\{scenario}.xml")
                #generate_coverage_report.report_generation(scenario,result_path,reports_path, test_scripts_path, executable_path)    
                generate_coverage_report.report_generation(data_folder='data/', results_folder=result_path+'\\coverage_reports', scenario=scenario)
                files = os.listdir(result_path)



                # if 'filename_to_class_mapping.xlsx' in files:
                #      generate_coverage_report.extract_coverage_info(xml_file_path, result_path, scenario)
                # else:
                #      generate_coverage_report.extract_coverage_info(xml_file_path,result_path,scenario,mapping=True)
        st.success("Test cases are executed and code coverage reports are generated!")
    
    if col2.button("Recommend impacted test cases"):
        final_changes = suggest_test_cases.git_diff(repo_path,result_path,start_commit)
        coverage_path = ""
        
        try:
            coverage_path = Path(os.path.join(result_path,"coverage_reports"))
            coverage_path.mkdir(parents=True, exist_ok=True)
            coverage_path.chmod(0o700)
        except Exception as e:
            print(e)
            
        recommendation = suggest_test_cases.recommend_test_cases(coverage_path,final_changes)
        
        try:
            with open(os.path.join(result_path,'recommended_test_cases.txt'), 'w') as f:
                f.write("Suggested test case/s \n")
                for i, ele in enumerate(recommendation, start=1):
                    f.write(f"{i}. {ele}\n")
        except Exception as e:
            print(e)
        
        s = ''
        for ele in list(recommendation):
            s += '- ' + ele + '\n'
        st.write('Suggested test case/s:')
        st.markdown(s)

if __name__ == "__main__":
    main()
