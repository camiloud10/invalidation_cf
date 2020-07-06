import boto3
import datetime

cloudfront = boto3.client('cloudfront')

response = cloudfront.create_invalidation( DistributionId='EL0L59ON22R4Z',
                                           InvalidationBatch={
                                               'Paths': {
                                                   'Quantity': 1,
                                                   'Items': [
                                                       '/content/*'
                                                   ],
                                               },
                                               'CallerReference': 'references-{}'.format(datetime.datetime.now())
                                            }
                                           )