"""
	A huge map of every Gengo API endpoint to a function definition in gengo-python.

	Parameters that need to be embedded in the URL are treated with mustaches, e.g:

	{{bert}}, etc

	When creating new endpoint definitions, keep in mind that the name of the mustache
	will be replaced with the keyword that gets passed in to the function at call time.

	i.e, in this case, if I pass bert = 47 to any function, {{bert}} will be replaced
	with 47, instead of defaulting to 1 (said defaulting takes place at conversion time).
"""

# Gengo API urls. {{version}} gets replaced with v1/etc
# at run time.
api_urls = {
	'sandbox': 'http://api.sandbox.mygengo.com/{{version}}',
	'base': 'http://api.gengo.com/{{version}}',
}

# The API endpoint 'table', 'database', 'hash', 'dictionary', whatever
# you'd like to call it. To keep things uber nice and organized, we secure away
# all the endpoints here with easily replaceable scenarios. Win!
apihash  = {
	# All Account-information based methods...
	'getAccountStats': {
		'url': '/account/stats',
		'method': 'GET',
	},
	'getAccountBalance': {
		'url': '/account/balance',
		'method': 'GET',
	},

	# Creating new translation requests.
	'postTranslationJob': {
		'url': '/translate/job',
		'method': 'POST',
	},
	'postTranslationJobs': {
		'url': '/translate/jobs',
		'method': 'POST',
	},

	# Updating an existing translation request.
	'updateTranslationJob': {
		'url': '/translate/job/{{id}}',
		'method': 'PUT',
	},

	# Viewing existing translation requests.
	'getTranslationJob': {
		'url': '/translate/job/{{id}}',
		'method': 'GET',
	},
	'getTranslationJobs': {
		'url': '/translate/jobs',
		'method': 'GET',
	},
	'getTranslationJobBatch': {
		'url': '/translate/jobs/{{id}}',
		'method': 'GET',
	},

	'getTranslationJobGroup': {
		'url': '/translate/jobs/group/{{id}}',
		'method': 'GET',
	},

	# Get a quote for how much a given job will cost.
	'determineTranslationCost': {
		'url': '/translate/service/quote',
		'method': 'POST',
        'upload': True, # with this being set the payload will be checked for file_path args and - if found - modified in a way so that opened file descriptors are passed to requests to do a multi part file upload. for now this is tied to jobs data only.
	},

	# Deal with comments and other metadata about a TranslationJob in progress.
	'postTranslationJobComment': {
		'url': '/translate/job/{{id}}/comment',
		'method': 'POST',
	},
	'getTranslationJobComments': {
		'url': '/translate/job/{{id}}/comments',
		'method': 'GET',
	},
	'getTranslationJobFeedback': {
		'url': '/translate/job/{{id}}/feedback',
		'method': 'GET',
	},
	'getTranslationJobRevisions': {
		'url': '/translate/job/{{id}}/revisions',
		'method': 'GET',
	},
	'getTranslationJobRevision': {
		'url': '/translate/job/{{id}}/revisions/{{revision_id}}',
		'method': 'GET',
	},
	'getTranslationJobPreviewImage': {
		'url': '/translate/job/{{id}}/preview',
		'method': 'GET',
	},

	# Delete a job...
	'deleteTranslationJob': {
		'url': '/translate/job/{{id}}',
		'method': 'DELETE',
	},

	# Translation Service language information. Holds information
	# about which languages can be converted to which, etc.
	'getServiceLanguagePairs': {
		'url': '/translate/service/language_pairs',
		'method': 'GET',
	},
	'getServiceLanguages': {
		'url': '/translate/service/languages',
		'method': 'GET',
	},

	# glossary stuff
	'getGlossaryList': {
		'url': '/translate/glossary',
		'method': 'GET',
	},

	'getGlossary': {
		'url': '/translate/glossary/{{id}}',
		'method': 'GET',
	},

	# order information
	'getTranslationOrderJobs': {
		'url': '/translate/order/{{id}}',
		'method': 'GET',
	},
}
