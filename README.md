## CEP Lookup Script with ViaCep API
![cep](cep.png)
> This simple script allows you to look up information about a **Brazilian ZIP code (CEP)** using the **ViaCep API**.

## How it works:

1. When you run the script, you need to provide a ZIP code **(CEP)**.


2. The script will make a request to the **ViaCep API** to get detailed information about the ZIP code.


3. The returned information will be saved in a JSON file. The file name will be the **CEP** followed by `_info.json`. For example, for CEP `12345678`, the generated file will be ``12345678_info.json``.
