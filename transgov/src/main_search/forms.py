from haystack.forms import FacetedSearchForm


class FacetedMeetingSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.categories = data.get('category', [])
        self.committees = data.get('committee', [])
        super(FacetedMeetingSearchForm, self).__init__(*args, **kwargs)

    def search(self):
        sqs = super(FacetedMeetingSearchForm, self).search()
        if self.categories:
            query = None
            for category in self.categories:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(category)
            sqs = sqs.narrow(u'category_exact:%s' % query)
        if self.committees:
            query = None
            for committee in self.committees:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(committee)
            sqs = sqs.narrow(u'committee_exact:%s' % query)
        return sqs
