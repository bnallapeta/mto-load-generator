# mto-load-generator

This project is designed to create tenants and namespaces on an OpenShift cluster, deploying a dummy application in each namespace to simulate resource consumption for testing purposes.

## Prerequisites

- Python 3.6+
- OpenShift CLI (`oc`) installed and configured
- OpenShift Python client
- Multi Tenant Operator (MTO) installed on the OpenShift cluster

## Installation

1. Clone the repository:

```bash
git clone https://github.com/bnallapeta/mto-load-generator.git
cd mto-load-generator
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Install MTO on the OpenShift cluster:

Follow the instructions in the [MTO documentation](https://docs.stakater.com/mto/latest/installation/openshift.html) to install MTO on the OpenShift cluster.

## Usage

Create tenants and namespaces:

```bash
python scripts/create_tenants.py --tenant-prefix=hogwarts --num-tenants=10
```

This command will create 10 tenants with the specified prefix and deploy the dummy application in each namespace.

## Project Structure

`main.py`: The main script that orchestrates the creation of tenants and deployment of dummy applications.
`templates/`: Contains YAML templates for tenants and dummy applications.
- `tenant_template.yaml`: Template for creating tenants.
- `dummy_app_template.yaml`: Template for deploying dummy applications.

`scripts/`: Contains scripts for creating tenants and deploying applications.
- `create_tenants.py`: Script to create tenants and namespaces.
- `deploy_dummy_app.py`: Script to deploy dummy applications.

## Contributing

Feel free to open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
