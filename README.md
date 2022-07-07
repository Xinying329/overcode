# overcode
OverCode's public repo (in development). See http://people.csail.mit.edu/elg/overcode for papers, posters, and talks.

# Basic Folder Tree - Only highlight the core folders + files might change by users
```bash
├── src
│   ├── pipeline_preprocessing.py
│   ├── pipeline.py
│   ├── run_pipeline.py
│   ├── student_code_solution
│   │   ├── code_submission_package.csv
│   ├── target
│   │   ├── data
│   │   │    ├── answer.py
│   │   │    ├── code_submission.py ONE PER FILE
│   │   │    ├── augmentedData
│   │   │    ├── pickleFiles
│   │   │    ├── tidyData
│   │   ├── testCase.py
│   │   ├── output
│   │   │    ├── correctOutput.json
│   │   │    ├── lines.json
│   │   │    ├── phrases.json
│   │   │    ├── solutions.json
│   │   │    ├── var_mappings.json
│   │   │    ├── solutions.json
│   │   │    ├── variables.json
├── view
│   ├── overcode_data
│   │   ├── target
│   ├── runServer.sh
└── README.md
```


## Running the pipeline
0. ```cd src```
1. Create a subdirectory under src named `target`
2. Extract solutions from a csv
```python testcase_making/extract_solutions_final.py student_code_solution/NAME_OF_THE_CODE_FILE target```
3. Find a correct submission and name it as `answer.py` in the subdirectory named `data`
4. Next to the `data` subdirectory, add a `testCase.py` file. Each line in this file is a single test case, i.e., a Python function call, prepended by the command `print`
5. Preprocessor: Execute the solutions on the testcases
    * In this repo's `src` directory, execute```python run_pipeline.py PATH_TO_TARGET_DIRECTORY --run-pre -n FUNCTION_NAME```
       * `-n FUNCTION_NAME` is optional, but helps us better tidy up solutions before execution
       * `--run-pre` means "run the preprocessor" which is what we call the code that executes and logs the behavior of solutions. It only needs to be done once, unless the test cases change.
6. Run the analysis pipeline on the results of executing the solutions
    * In this repo's `src` directory, execute ```python run_pipeline.py PATH_TO_TARGET_DIRECTORY --run-pipeline```

## View
0. ```cd ui```
1. copy the `target` directory above as a subdirectory in `overcode_data` under `ui`
2. run a server in the folder from the commandline, and give ?src=DATASET where DATASET is a key in the config.json file.
