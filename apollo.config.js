module.exports = {
  client: {
    addTypename: true,
    includes: [
      'sellor/static/dashboard-next/**/*.ts',
      'sellor/static/dashboard-next/**/*.tsx'
    ],
    name: 'storefront',
    service: {
      localSchemaFile: 'sellor/graphql/schema.graphql',
      name: 'sellor'
    }
  }
};
