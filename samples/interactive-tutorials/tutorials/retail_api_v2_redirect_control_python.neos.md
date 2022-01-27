<walkthrough-metadata>
  <meta name="title" content="Redirect control tutorial" />
  <meta name="description" content="The redirect control lets you specify a URL to redirect users to when they search for a specific query." />
  <meta name="component_id" content="593554" />
</walkthrough-metadata>

# Redirect control tutorial

## Get started

The redirect control lets you specify a URL to redirect users to when they search for a specific query.
Because we are not able to check its effect on the [Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate), we will test it in the Cloud Shell. Make sure that you've created and attached the redirect control to the serving config. You can find the step-by-step instructions on how to do it in the [Creating and Managing Controls tutorial](https://cloud.google.com/retail/docs/manage-controls).


<walkthrough-tutorial-duration duration="7"></walkthrough-tutorial-duration>

## Get started with Google Cloud Retail

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

### Select your project and enable the Retail API

Google Cloud organizes resources into projects. This lets you
collect all the related resources for a single application in one place.

If you don't have a Google Cloud project yet or you're not the owner of an existing one, you can
[create a new project](https://console.cloud.google.com/projectcreate).

After the project is created, set your PROJECT_ID to a ```project``` variable.
1. Run the following command in Terminal:
    ```bash
    gcloud config set project <YOUR_PROJECT_ID>
    ```

1. Check that the Retail API is enabled for your Project in the [Admin Console](https://console.cloud.google.com/ai/retail/).

### Set up authentication

To run a code sample from the Cloud Shell, you need to be authenticated using the service account credentials.

1. Login with your user credentials.
    ```bash
    gcloud auth login
    ```

1. Type `Y` and press **Enter**. Click the link in Terminal. A browser window should appear asking you to log in using your Gmail account.

1. Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

1. Upload your service account key JSON file and use it to activate the service account:

    ```bash
    gcloud iam service-accounts keys create ~/key.json --iam-account <YOUR_SERVICE_ACCOUNT_EMAIL>
    ```

    ```bash
    gcloud auth activate-service-account --key-file  ~/key.json
    ```

1. Set key as the GOOGLE_APPLICATION_CREDENTIALS environment variable to be used for requesting the Retail API:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS=~/key.json
    ```

**Note**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

### Set the PROJECT_NUMBER and PROJECT_ID environment variables

Because you are going to run the code samples in your own Google Cloud project, you should specify the **project_number** and **project_id** as environment variables. It will be used in every request to the Retail API.

1. Find the project number and project ID in the Project Info card displayed on **Home/Dashboard**.

1. Set **project_number** with the following command:
    ```bash
    export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
    ```
1. Set **project_id** with the following command:
    ```bash
    export PROJECT_ID=<YOUR_PROJECT_ID>
    ```

### Install Google Cloud Retail libraries

To run Python code samples for the Retail API tutorial, you need to set up your virtual environment.

1. Run the following commands in a Terminal to create an isolated Python environment:
    ```bash
    pip install virtualenv
    virtualenv myenv
    source myenv/bin/activate
    ```
1. Next, install Google packages:
    ```bash
    pip install google
    pip install google-cloud-retail
    pip install google.cloud.storage
    pip install google.cloud.bigquery

    ```

## Clone the Retail code samples

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

Clone the Git repository with all the code samples to learn the Retail features and check them in action.

<!-- TODO(ianan): change the repository link -->
1. Run the following command in the Terminal:
    ```bash
    git clone https://github.com/googleapis/python-retail.git
    ```

    The code samples for each of the Retail services are stored in different directories.

1. Go to the ```samples/interactive-tutorials``` directory. This is our starting point to run more commands.
    ```bash
    cd samples/interactive-tutorials
    ```

## Import catalog data

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

### Upload catalog data to Cloud Storage

There is a JSON file with valid products prepared in the `resources` directory:
`resouces/products.json`.

Another file, `resources/products_some_invalid.json`, contains both valid and invalid products, and you will use it to check the error handling.

In your own project you need to create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique. For convenience, you can name it `<YOUR_PROJECT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file, run the following command in the Terminal:

    ```bash
    python product/setup/products_create_gcs_bucket.py
    ```

    Now you can see the bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the files are uploaded.

1. The name of the created Cloud Storage bucket is printed in the Terminal. Copy the name and set it as the environment variable `BUCKET_NAME`:

    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

### Import products to the Retail catalog

To import the prepared products to a catalog, run the following command in the Terminal:

```bash
python product/import_products_gcs.py
```

## Configure search to use the redirect control

1. Open
<walkthrough-editor-select-regex filePath="cloudshell_open/python-retail/samples/interactive-tutorials/search/search_simple_query.py" regex="TRY DIFFERENT QUERY PHRASES HERE">search_simple_query.py</walkthrough-editor-select-regex> to review the request.

1. Change the query variable to match the one you configured as a query term in your redirect control:

    ```query_phrase = "<YOUR_QUERY_TERM>"```

The next step is to configure the Search Service to use the serving config that has the redirect control attached.

## Configure search to use the serving config

1. In the code sample, find the <walkthrough-editor-select-regex filePath="cloudshell_open/python-retail/samples/interactive-tutorials/search/search_simple_query.py" regex="default_search_placement">variable</walkthrough-editor-select-regex>.

    Before you apply the changes, it should look like this:

    ```
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"
    ```

1. Replace the `default_search` part to the ID of your serving config.

1. After you apply the changes, it should look like this:

    ```
    default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/<YOUR_SERVING_CONFIG_ID>"
    ```

## Redirect control testing

We want to check the effect of the redirect control printed in our console.

1. Go to the bottom of the code sample and find the following code fragment:

    ```
    print("---search response---")
    ```

1. Add the following piece of code below:

    ```
    print("redirect uri: " + search_response.redirect_uri)
    ```

1. To execute our code sample, run the following command in the Terminal:
    ```bash
    python search/search_simple_query.py
    ```
1. You should see the redirect URL printed in the Terminal.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the redirect controls by yourself.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
