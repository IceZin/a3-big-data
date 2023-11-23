from sqlalchemy import select
from sqlalchemy.orm import (
    Session as PgSession,
)
from sqlalchemy.exc import SQLAlchemyError

from . import engine, Country


class CountryQueries:
    @staticmethod
    def get_by_uuid(country_id: int) -> Country:
        with PgSession(engine) as session:
            query = select(Country).where(Country.id == country_id)
            result = session.execute(query).first()
            return result[0]
        
    @staticmethod
    def insert(country: Country) -> int:
        with PgSession(engine) as pg_session:
            pg_session.add(country)

            try:
                pg_session.commit()
            except SQLAlchemyError as e:
                print(e)
                return None
            finally:
                return country.code
